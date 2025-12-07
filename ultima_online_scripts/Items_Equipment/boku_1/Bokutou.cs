using System;
using System.Text;
using Server;
using Server.Mobiles;
using Server.ContextMenus;
using System.Collections;
using Server.Gumps;

namespace Server.Items
{
	[FlipableAttribute( 0x13FE, 0x13FF )]
	public class LevelBokutou : BaseSword, ILevelable // ILevelable is the interface that gives us all the leveling functionality
	{
		/* This is the type array that contains all 
		 * the monster types you want your item to 
		 * gain experience from */

		private static Type[] m_Types = new Type[]
				{
					typeof( Cyclops ),
					typeof( Titan ),
					typeof( Dragon ),
					typeof( Drake ),
					typeof( ShadowWyrm ),
					typeof( AncientWyrm ),
					typeof( OrcBrute ),
					typeof( OgreLord ),
					typeof( LichLord ),
					typeof( AncientLich )
				};
		
		public override WeaponAbility PrimaryAbility{ get{ return WeaponAbility.DoubleStrike; } }
		public override WeaponAbility SecondaryAbility{ get{ return WeaponAbility.ArmorIgnore; } }

		public override int AosStrengthReq{ get{ return 25; } }
		public override int AosMinDamage{ get{ return 11; } }
		public override int AosMaxDamage{ get{ return 13; } }
		public override int AosSpeed{ get{ return 46; } }

		public override int OldStrengthReq{ get{ return 10; } }
		public override int OldMinDamage{ get{ return 5; } }
		public override int OldMaxDamage{ get{ return 26; } }
		public override int OldSpeed{ get{ return 58; } }

		public override int DefHitSound{ get{ return 0x23B; } }
		public override int DefMissSound{ get{ return 0x23A; } }

		public override int InitMinHits{ get{ return 31; } }
		public override int InitMaxHits{ get{ return 90; } }

		/* These private variables store the exp and
		 * level for the item */
		private int m_Experience;
		private int m_Level;

		[Constructable]
		public LevelBokutou() : base( 0x13FF ) 
		{
			Hue = 0x27F;
			Name = "Bokutou";
			/* Invalidate the level and refresh the item props
			 * Extremely important to call this method */

			LevelItemManager.InvalidateLevel( this );
		}

		public LevelBokutou( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 );

			// DONT FORGET TO SERIALIZE LEVEL AND EXPERIENCE
			writer.Write( m_Experience );
			writer.Write( m_Level );
		}
		
		public override void Deserialize(GenericReader reader)
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
			
			// DONT FORGET TO DESERIALIZE LEVEL AND EXPERIENCE
			m_Experience = reader.ReadInt();
			m_Level = reader.ReadInt();
		}

		public override void GetProperties(ObjectPropertyList list)
		{
			base.GetProperties (list);

			/* My implementation of adding them to the props grid
			 * If you use a non aos server, you might need to
			 * override GetNameProperties or you can use 
			 * GetHtml()( discussed later in script ) and 
			 * implement it into the gump. */

			list.Add( 1060658, "Level\t{0}", m_Level );
			list.Add( 1060659, "Experience\t{0}", m_Experience );
		}

		public override void GetContextMenuEntries(Mobile from, ArrayList list)
		{
			base.GetContextMenuEntries (from, list);

			/* Context Menu Entry to display the gump w/ 
			 * all info */

			list.Add( new LevelInfoEntry( this ) );
		}

		// ILevelable Members that MUST be implemented
		#region ILevelable Members

		/* This one will return our private m_Experience 
		 * variable */
		[CommandProperty( AccessLevel.GameMaster )]
		public int Experience
		{
			get
			{
				return m_Experience;
			}
			set
			{
				m_Experience = value;

				// Beta 2 addition, this keeps gms from setting
				// the level to an outrageous value
				if ( m_Experience > LevelItemManager.ExpTable[LevelItemManager.Levels - 1] )
					m_Experience = LevelItemManager.ExpTable[LevelItemManager.Levels - 1];

				// Anytime exp is changed, call this method
				LevelItemManager.InvalidateLevel( this );
			}
		}

		/* This one will return our private m_Level 
		 * variable */
		[CommandProperty( AccessLevel.GameMaster )]
		public int Level
		{
			get
			{
				return m_Level;
			}
			set
			{
				// Beta 2 addition, this keeps gms from setting
				// the level to an outrageous value
				if ( value > LevelItemManager.Levels )
					value = LevelItemManager.Levels;

				// Beta 2 addition, this keeps gms from setting
				// the level to 0 or a negative value
				if ( value < 1 )
					value = 1;

				// THIS IS EXTREMELY IMPORTANT
				if ( m_Level != value )
				{
					int oldLevel = m_Level;

					m_Level = value;

					// Anytime level changes, call this method
					OnLevel( oldLevel, m_Level );
				}
			}
		}

		/* This ILevelable member returns which types we want
		 * our item to level on. So, we'll return our private
		 * static array we declared earlier. */
		public Type[] Types
		{
			get
			{
				return m_Types;
			}
		}

		/// <summary>
		/// This method is called when the Item's level has changed
		/// </summary>
		/// <param name="oldLevel">The item's old level</param>
		/// <param name="newLevel">The item's new level</param>
		public void OnLevel( int oldLevel, int newLevel )
		{
			/* This is where we control all our props 
			 * and their maximum value. */

			WeaponAttributes.HitEnergyArea = LevelItemManager.CalculateProperty( 75, m_Level );


			/* for Non AOS servers, you would need to change it a tad bit more.
			 * Heres a basic example of weapon damage
			 * 
			 * this.DamageLevel = LevelItemManager.CalculateProperty( (int)WeaponDamageLevel.Vanq, m_Level ) );
			 */


			Attributes.BonusStr = LevelItemManager.CalculateProperty( 15, m_Level );
			Attributes.BonusDex = LevelItemManager.CalculateProperty( 15, m_Level );
			Attributes.AttackChance = LevelItemManager.CalculateProperty( 25, m_Level );
			Attributes.WeaponDamage = LevelItemManager.CalculateProperty( 75, m_Level );
			Attributes.WeaponSpeed = LevelItemManager.CalculateProperty( 35, m_Level );
			Attributes.Luck = LevelItemManager.CalculateProperty( 100, m_Level );
			
			
		}

		/// <summary>
		/// This gets the Html Formatted Info to display in the
		/// information gump.
		/// </summary>
		/// <returns></returns>
		public string GetHtml()
		{
			/* This can be done just about any way you want, just
			 * be sure to do it in html format. StringBuilder is
			 * in the System.Text namespace so if you use it,
			 * don't forget to add using System.Text; at the top
			 * of your script. */

			StringBuilder builder = new StringBuilder();

			builder.Append( "<br>" );
			builder.Append( "<div align=center><i>ENHANCEMENTS</i></div>" );
		
			builder.Append( "Bonus Strength: 15<br>" );
			builder.Append( "Bonus Dexterity: 15<br>" );
			builder.Append( "Hit Energy Area: 100%<br>" );
			builder.Append( "Attack Chance: 25%<br>" );
			builder.Append( "Increase Damage: 75%<br>" );
			builder.Append( "Increase Speed: 35%<br>" );
			builder.Append( "Increase Luck: 100<br>" );

			return builder.ToString();
		}

		#endregion
	}

	
     }