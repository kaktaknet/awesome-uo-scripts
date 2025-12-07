using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a Yamandon corpse" )]
	public class Yamandon : BaseCreature
	{
		public override WeaponAbility GetWeaponAbility()	
            {
                  return WeaponAbility.BleedAttack;
            } 

		[Constructable]
		public Yamandon() : base( AIType.AI_Melee, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{
			Name = "a Yamandon";
			Body = 249;
			BaseSoundID = 634;

			SetStr( 785, 930 );
			SetDex( 250, 365 );
			SetInt( 100, 120 );

			SetHits( 1600, 1800 );
			SetMana( 100, 120 );
			SetStam( 250, 365 );

			SetDamage( 90, 167 );

			SetDamageType( ResistanceType.Physical, 70 ); 
     		    	SetDamageType( ResistanceType.Poison, 20 ); 
     		    	SetDamageType( ResistanceType.Energy, 10 ); 

			SetResistance( ResistanceType.Physical, 65, 85 );
			SetResistance( ResistanceType.Fire, 70, 90 );
			SetResistance( ResistanceType.Cold, 50, 70 );
			SetResistance( ResistanceType.Poison, 50, 70 );
			SetResistance( ResistanceType.Energy, 50, 70 );

			SetSkill( SkillName.MagicResist, 115.0, 135.0 );
			SetSkill( SkillName.Tactics, 115.0, 135.0 );
			SetSkill( SkillName.Wrestling, 110.0, 135.0 );
			SetSkill( SkillName.Poisoning, 120.0, 140.0 );


			Fame = 15000;
			Karma = -15000;
			
			Tamable = false;
					
         PackGold( 2000, 2500 ); 
         PackMagicItems( 5, 15 );


 
		}
		
		public override void GenerateLoot()
			
		{
			AddLoot( LootPack.FilthyRich );
			AddLoot( LootPack.FilthyRich );
			AddLoot( LootPack.MedScrolls, 1 );
		}
		public override Poison PoisonImmune{ get{ return Poison.Lethal; } }
		public override Poison HitPoison{ get{ return Poison.Lethal; } }
		public override FoodType FavoriteFood{ get{ return FoodType.Fish; } }
		public override int TreasureMapLevel{ get{ return 5; } }
		public override int Hides{ get{ return 20; } }
		public override HideType HideType{ get{ return HideType.Horned; } }
		public override int Scales{ get{ return 5; } }
		public override ScaleType ScaleType{ get{ return ( Body == 60 ? ScaleType.Yellow : ScaleType.Red ); } }

                public Yamandon( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
		}
	}
}