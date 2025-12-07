using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a Lady of the Snow corpse" )]
	public class LadyoftheSnow : BaseCreature
	{
		public override WeaponAbility GetWeaponAbility()	
            {
                  return WeaponAbility.BleedAttack;
            } 

		[Constructable]
		public LadyoftheSnow() : base( AIType.AI_Melee, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{
			Name = "a Lady of the Snow";
			Body = 252;
			BaseSoundID = 0x4B0;

			SetStr( 275, 305 );
			SetDex( 105, 125 );
			SetInt( 470, 490 );

			SetHits( 595, 625 );
			SetMana( 470, 490 );
			SetStam( 105, 125 );

			SetDamage( 32, 49 );

			SetDamageType( ResistanceType.Physical, 20 ); 
	         	SetDamageType( ResistanceType.Cold, 80 ); 

			SetResistance( ResistanceType.Physical, 45, 55 );
			SetResistance( ResistanceType.Fire, 40, 55 );
			SetResistance( ResistanceType.Cold, 70, 90 );
			SetResistance( ResistanceType.Poison, 60, 70 );
			SetResistance( ResistanceType.Energy, 70, 85 );

			SetSkill( SkillName.MagicResist, 90.0, 105.0 );
			SetSkill( SkillName.Tactics, 85.0, 100.0 );
			SetSkill( SkillName.Wrestling, 85.0, 100.0 );
			SetSkill( SkillName.Magery, 95.0, 110.0 );
			SetSkill( SkillName.Meditation, 85.0, 90.0 );


			Fame = 1500;
			Karma = 1500;
			
			Tamable = false;

			
         PackGold( 800, 1000 ); 
         PackMagicItems( 1, 5 );
		 PackReg( 5, 14 );
 
		}
		
		public override void GenerateLoot()
		{
			AddLoot( LootPack.MedScrolls, 1 );
		}
		public override Poison PoisonImmune{ get{ return Poison.Deadly; } }
		public override Poison HitPoison{ get{ return Poison.Deadly; } }

                public LadyoftheSnow( Serial serial ) : base( serial )
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